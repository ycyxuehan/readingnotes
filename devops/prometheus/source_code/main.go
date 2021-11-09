package main

import (
	"log"
	"net/http"

	"github.com/prometheus/client_golang/prometheus/promhttp"
)


func runHTTPServer()error{
	http.Handle("/metrics", promhttp.Handler())
	http.HandleFunc("/", func (w http.ResponseWriter, r *http.Request){
		w.Write([]byte("hello world!"))
	})
	return http.ListenAndServe("localhost:8080", nil)
}

func main(){
	err := runHTTPServer()
	if err != nil {
		log.Fatal(err)
	}
}