package main

import (
	"net/http"
	"github.com/labstack/echo"
)

type User struct {
    Id  string  `json:"id"`
    Nick_name  string  `json:"nick_name"`
    Url  string  `json:"url"`
    Lang  string  `json:"lang"`
}

func user_create(c echo.Context)error{
    u := new(User)
    if err := c.Bind(u); err != nil {
        return err
    }
    return c.JSON(http.StatusCreated, u)
}

func main() {
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})
	e.POST("/usercreate",user_create)
	e.Logger.Fatal(e.Start(":1323"))

}