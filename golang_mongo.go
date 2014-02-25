package main

import (
        "fmt"
        "labix.org/v2/mgo"
        "labix.org/v2/mgo/bson"
        "log"
        "net/http"
        "runtime"
)

type Data struct {
	Data string
}

var session *mgo.Session

func main() {

	// runtime.GOMAXPROCS(runtime.NumCPU())
    runtime.GOMAXPROCS(1)

	var err error
    session, err = mgo.Dial("127.0.0.1")
    if err != nil {
            panic(err)
    }
    defer session.Close()

    // Optional. Switch the session to a monotonic behavior.
    session.SetMode(mgo.Monotonic, true)

    c := session.DB("documents").C("items")
    query := bson.M{}
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		result := Data{}
	    err = c.Find(query).One(&result)
	    if err != nil {
            panic(err)
	    }
		fmt.Fprintf(w, "%s", result.Data)
	})

    log.Fatal(http.ListenAndServe(":8080", nil))
}

