package hello

const testVersion = 2

// Function printing hello, name if a name is given or hello world if it is not
func HelloWorld(name string) string {
	if name == "" {
		return "Hello, World!"
	} else {
		return "Hello, " + name + "!"
	}
}
