package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/pkg/browser"
)

func search(word string) {
	url := "https://www.youtube.com/results?search_query=" + word
	err := browser.OpenURL(url)
	if err != nil {
		panic(err)
	}

}

func main() {

	word := os.Args[1:]
	cmdLineInput := strings.Join(word, " ")

	if len(cmdLineInput) > 0 {
		search(cmdLineInput)
		return
	} else {
		var search_word string
		fmt.Println("what do you want to watch on youtube: ")
		scanner := bufio.NewScanner(os.Stdin)
		scanner.Scan()
		search_word = scanner.Text()
		search(search_word)
		return
	}

}
