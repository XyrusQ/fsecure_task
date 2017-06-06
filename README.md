# magic_app

## How to
1. Install things from section "Environment"
2. Start server
3. Open http://localhost:8080 (default values)
4. Enter values in lines and press "Calculate!"

## Environment:
- Ruby 2.4.0 + dependencies + RVM (https://tecadmin.net/install-ruby-2-4-centos-rvm/)
- Rack 2.0.3 (gem install rack)
- Python 2.7
- Go 1.8.3 (https://www.digitalocean.com/community/tutorials/how-to-install-go-1-7-on-centos-7)
- CentOS 7 (I have used VMware Workstation)
- Git 1.8.3.1
- RPN Calculator from https://github.com/irlndts/go-rpn (with few modifications)


### Useful commands
Build .so and .h files:
```
go build -buildmode=c-shared -o librpn.so src/librpn.go
```

Install Calculator:
```
go install github.com/irlndts/go-rpn/
```

Start server:
```
ruby rpn_app.rb
[2017-06-05 21:07:36] INFO  WEBrick 1.3.1
[2017-06-05 21:07:36] INFO  ruby 2.4.0 (2016-12-24) [x86_64-linux]
[2017-06-05 21:07:36] INFO  WEBrick::HTTPServer#start: pid=32755 port=8080
```

### Go Envs
```
export GOROOT=/usr/local/go
export GOPATH="$PATH_TO_YOUR_PROJECT/src"
export GOBIN="$PATH_TO_YOUR_PROJECT/bin"
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```

## Logs
You can find two example log files:
- 2017-06-05_rpn_api.log (development stage + last version)
- 2017-06-04_rpn_api.log (development stage)

## Example:
Input:
```
2
3 4 +
5 1 2 + 4 * + 3 -
```

Output:
```
7.000000, 0.105418
14.000000, 0.000081
```

## RPN Calculator Modifications
- use float64 instead of int (in Calc, operation and pop functions)
- new import "math"
- use ParseFloat instead of Atoi (strconv package)
- use math.Pow(b, a) instead of a^b (due to invalid operation: a ^ b (operator ^ not defined on float64))


## Spent time
Day 1 (31.05) - Education
- 21:30 - 21:45 (RPN)
- 21:45 - 23:45 (Django, Rack, Ruby on Rails, REST, RPN in Go, WebServices, API)

Day 2 (04.06) - Environment + Coding + Education
- 13:25 - 14:15 (Install Ruby and Rack)
- 14:15 - 16:20 (Rack, HTML, JSON, Python)
- 17:50 - 18:05 (Install Go)
- 18:05 - 23:05 (Go, Workers, CPython, Python, c-shared)

Day 3 (05.06) - Coding + Education
- 18:15 - 22:15 (Go, JSON, Python, Rack, Modifications in Calculator)
- 22:15 - 23:55 (GitHub, Commits, Readme)
