package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strings"
)

func openApplication(appName string) error {
	switch runtime.GOOS {
	case "darwin":
		fmt.Println("Running on macOS")
		cmd := exec.Command("open", "-a", appName) // macOS command to open app
		if err := cmd.Run(); err != nil {
			fmt.Println("Error opening app on macOS:", err)
		}
		return cmd.Run()

	case "windows":
		fmt.Println("Running on Windows")
		cmd := exec.Command("cmd", "/C", "start", appName)
		return cmd.Run()
	}
	return nil
}

func open(appName string) {
	err := openApplication(appName)
	if err != nil {
		fmt.Printf("Failed to open application %s: %v\n", appName, err)
	} else {
		fmt.Printf("Application %s opened successfully\n", appName)
	}
}

func main() {
	word := os.Args[1:]
	cmdLineInput := strings.Join(word, " ")

	if len(cmdLineInput) > 0 {
		open(cmdLineInput)
		return
	} else {
		var search_word string
		fmt.Println("what app do you want to open: ")
		scanner := bufio.NewScanner(os.Stdin)
		scanner.Scan()
		search_word = scanner.Text()
		open(search_word)
		return
	}

}
