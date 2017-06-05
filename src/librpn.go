//librpn.go
package main

import "C"

import (
	"fmt"
	"github.com/irlndts/go-rpn"
)

var jobs = make(chan string, 20)
var results = make(chan float64, 20)

func worker(jobs <-chan string, results chan<- float64) {
    for j := range jobs {
        rpn_result, rpn_err := rpn.Calc(j)
        if rpn_err != nil{
            fmt.Println(rpn_err)
        }
        results <- rpn_result
    }
}

//export start_job
func start_job(rpn_str string) float64 {

    go worker(jobs, results)

    jobs <- rpn_str

    rpn_res := <-results

    return rpn_res
}

func main() {}
