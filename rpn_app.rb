# rpn_app.rb
require 'rack'
require 'rack/server'
require 'json'

class RPN
  def index_page

    html = "<!DOCTYPE html>
            <html>
            <head>
            <title>RPN Application</title>
            </head>
            <body>

            <form action='/calculate' method='post'>
            Input:<br>
            <textarea name='input_rpn' cols='70' rows='7'></textarea><br>
            <input type='submit' value='Calculate!'>
            </form>

            </body>
            </html>"
    [200, {"Content-Type" => "text/html"}, [html]]
  end


  def calculate_rpn(parameters)
    temp_json_file = Tempfile.new(["rpn_temp", ".json"])
    temp_json_file.write(parameters.to_json)
    temp_json_file.flush

    python_api_cmd = "python rpn_api.py " + temp_json_file.path
    python_api_result = JSON.parse(`#{python_api_cmd}`)

    temp_json_file.close
    temp_json_file.unlink

    rpn_output = ""

    for rpn_pair in python_api_result.keys
        rpn_output += "%f, %f<br>" % [python_api_result[rpn_pair]["result"], python_api_result[rpn_pair]["time"]]
    end

    [200, {"Content-Type" => "text/html"}, [rpn_output]]
  end
end

class RPNApp
  def self.call(env)
    request = Rack::Request.new env
    
    if request.env["REQUEST_PATH"] == "/calculate" and request.env["REQUEST_METHOD"] == "POST"
      RPN.new.calculate_rpn(request.params)
    else
      RPN.new.index_page
    end
  end
end

Rack::Server.start :app => RPNApp
