# Sonic Pi をヘッドレスで 1 回だけ起動しておき、標準入力の命令でコードを鳴らす常駐プレイヤー(DAW の ▶ 用)。
#   ruby sonicpi_player.rb
# 標準入力(1 行 1 命令):  PLAY /path/code.rb  = 鳴らしているものを止めて、そのコードを鳴らす / STOP = 止める / QUIT = 終了
# 標準出力: READY(起動完了)/ PLAYING / STOPPED / ERRORS ...(Sonic Pi のエラー)
# 標準入力が閉じたら(親が終了したら)自分で止まる。起動した daemon・エンジンは、自分の子孫だけを止める。
root = ENV["SONIC_PI_APP"] || "/Applications/Sonic Pi.app"
require File.join(root, "Contents/Resources/app/server/ruby/bin/headless_boot")

def descendants(pid)
  kids = `pgrep -P #{pid}`.split.map(&:to_i)
  kids + kids.flat_map { |k| descendants(k) }
end

def finish(code)
  descendants(Process.pid).each { |k| Process.kill("TERM", k) rescue nil }
  exit!(code)
end

boot = SonicPi::HeadlessBoot.new.boot!
seen = 0
puts "READY"
$stdout.flush

while (line = $stdin.gets)
  cmd, arg = line.strip.split(" ", 2)
  case cmd
  when "PLAY"
    boot.stop_all
    sleep 0.15
    unless arg && File.file?(arg)
      puts "ERRORS no such file: #{arg}"
      $stdout.flush
      next
    end
    boot.run("eval_file #{File.expand_path(arg).inspect}")
    sleep 0.3
    puts(boot.errors.size > seen ? "ERRORS #{boot.errors[seen..].join(' | ')}" : "PLAYING")
    seen = boot.errors.size
  when "STOP"
    boot.stop_all
    puts "STOPPED"
  when "QUIT"
    break
  end
  $stdout.flush
end
boot.stop_all
sleep 0.3
finish(0)
