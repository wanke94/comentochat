package main

import (
	"context"
	"log"
	"os"
	"time"

	"google.golang.org/grpc"
	pb "comentochat/user"
)

func main() {
    conn, err := grpc.Dial("localhost:8000", grpc.WithInsecure(), grpc.WithBlcok())
    if err != nil {
        log.Fatalf("did not connect: %v", err)
    }
    defer conn.Close()
    c := pb.NewGetUserClient(conn)

    ctx, cancel := context.WithTimeout(context.Background(), time.Second)
    defer cancel()

     r, err := c.Get(ctx, &pb.UserReqeust{Profile: "dev"})
    if err != nil {
        log.Fatalf("could not request: %v", err)
    }

    log.Printf("Config: %v", r)
    //e := echo.New()
    //e.POST("/", GetUser)
    //e.Logger.Fatal(e.Start(":1323"))
}