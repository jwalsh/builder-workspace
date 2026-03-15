package main

import (
	"fmt"
	"os"
	"strings"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

// Pattern represents a software design pattern
type Pattern struct {
	Name     string
	Category string // creational, structural, behavioral
	Intent   string
	When     string
	Example  string
}

var patterns = []Pattern{
	{Name: "Singleton", Category: "creational", Intent: "Ensure a class has only one instance and provide a global point of access to it.", When: "Exactly one instance of a class is needed to coordinate actions across the system.", Example: "Database connection pool, Logger, Configuration manager"},
	{Name: "Factory Method", Category: "creational", Intent: "Define an interface for creating an object, but let subclasses decide which class to instantiate.", When: "A class can't anticipate the class of objects it must create.", Example: "Document creators (PDF, HTML, Markdown), Transport providers"},
	{Name: "Abstract Factory", Category: "creational", Intent: "Provide an interface for creating families of related objects without specifying their concrete classes.", When: "A system should be independent of how its products are created.", Example: "UI toolkit (buttons, menus for Mac/Windows/Linux)"},
	{Name: "Builder", Category: "creational", Intent: "Separate the construction of a complex object from its representation.", When: "The algorithm for creating a complex object should be independent of the parts.", Example: "Query builder, Meal builder, HTML document builder"},
	{Name: "Prototype", Category: "creational", Intent: "Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.", When: "Classes to instantiate are specified at run-time.", Example: "Cloning game objects, Document templates"},
	{Name: "Adapter", Category: "structural", Intent: "Convert the interface of a class into another interface clients expect.", When: "You want to use an existing class, but its interface doesn't match what you need.", Example: "XML to JSON adapter, Legacy API wrapper"},
	{Name: "Bridge", Category: "structural", Intent: "Decouple an abstraction from its implementation so the two can vary independently.", When: "You want to avoid a permanent binding between an abstraction and its implementation.", Example: "Shape rendering (vector vs raster), Remote controls"},
	{Name: "Composite", Category: "structural", Intent: "Compose objects into tree structures to represent part-whole hierarchies.", When: "You want clients to treat individual objects and compositions uniformly.", Example: "File system (files and directories), UI component trees"},
	{Name: "Decorator", Category: "structural", Intent: "Attach additional responsibilities to an object dynamically.", When: "You need to add responsibilities to individual objects without affecting other objects.", Example: "I/O streams, Middleware chains, Logging wrappers"},
	{Name: "Facade", Category: "structural", Intent: "Provide a unified interface to a set of interfaces in a subsystem.", When: "You want to provide a simple interface to a complex subsystem.", Example: "Compiler facade, Home theater system"},
	{Name: "Observer", Category: "behavioral", Intent: "Define a one-to-many dependency so that when one object changes state, all its dependents are notified.", When: "A change to one object requires changing others, and you don't know how many objects need to change.", Example: "Event systems, MVC pattern, Pub/sub messaging"},
	{Name: "Strategy", Category: "behavioral", Intent: "Define a family of algorithms, encapsulate each one, and make them interchangeable.", When: "You need different variants of an algorithm.", Example: "Sorting algorithms, Payment methods, Compression strategies"},
	{Name: "Command", Category: "behavioral", Intent: "Encapsulate a request as an object, letting you parameterize clients with different requests.", When: "You want to parameterize objects by an action to perform.", Example: "Undo/redo, Job queues, Macro recording"},
	{Name: "State", Category: "behavioral", Intent: "Allow an object to alter its behavior when its internal state changes.", When: "An object's behavior depends on its state, and it must change behavior at run-time.", Example: "TCP connection states, Order status, Media player"},
	{Name: "Template Method", Category: "behavioral", Intent: "Define the skeleton of an algorithm, deferring some steps to subclasses.", When: "You want to let subclasses redefine certain steps of an algorithm without changing its structure.", Example: "Data mining (CSV, DB, PDF), Game AI turns"},
}

var (
	titleStyle    = lipgloss.NewStyle().Bold(true).Foreground(lipgloss.Color("205"))
	categoryStyle = lipgloss.NewStyle().Foreground(lipgloss.Color("240"))
	selectedStyle = lipgloss.NewStyle().Bold(true).Foreground(lipgloss.Color("86"))
	detailStyle   = lipgloss.NewStyle().Padding(1, 2).Border(lipgloss.RoundedBorder()).BorderForeground(lipgloss.Color("62"))
	helpStyle     = lipgloss.NewStyle().Foreground(lipgloss.Color("241"))
)

type model struct {
	patterns   []Pattern
	cursor     int
	filter     string // "", "creational", "structural", "behavioral"
	showDetail bool
}

func (m model) filtered() []Pattern {
	if m.filter == "" {
		return m.patterns
	}
	var out []Pattern
	for _, p := range m.patterns {
		if p.Category == m.filter {
			out = append(out, p)
		}
	}
	return out
}

func (m model) Init() tea.Cmd { return nil }

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		switch msg.String() {
		case "q", "ctrl+c":
			return m, tea.Quit
		case "j", "down":
			if m.cursor < len(m.filtered())-1 {
				m.cursor++
			}
		case "k", "up":
			if m.cursor > 0 {
				m.cursor--
			}
		case "enter", " ":
			m.showDetail = !m.showDetail
		case "1":
			m.filter, m.cursor = "", 0
		case "2":
			m.filter, m.cursor = "creational", 0
		case "3":
			m.filter, m.cursor = "structural", 0
		case "4":
			m.filter, m.cursor = "behavioral", 0
		case "?":
			m.showDetail = !m.showDetail
		}
	}
	return m, nil
}

func (m model) View() string {
	var b strings.Builder

	b.WriteString(titleStyle.Render("Design Pattern Explorer"))
	b.WriteString("\n")

	// Filter tabs
	filters := []struct{ key, label, value string }{
		{"1", "All", ""},
		{"2", "Creational", "creational"},
		{"3", "Structural", "structural"},
		{"4", "Behavioral", "behavioral"},
	}
	for _, f := range filters {
		label := fmt.Sprintf(" [%s] %s ", f.key, f.label)
		if m.filter == f.value {
			b.WriteString(selectedStyle.Render(label))
		} else {
			b.WriteString(categoryStyle.Render(label))
		}
	}
	b.WriteString("\n\n")

	filtered := m.filtered()
	for i, p := range filtered {
		cursor := "  "
		if i == m.cursor {
			cursor = "> "
		}
		name := p.Name
		if i == m.cursor {
			name = selectedStyle.Render(p.Name)
		}
		cat := categoryStyle.Render(fmt.Sprintf("[%s]", p.Category))
		b.WriteString(fmt.Sprintf("%s%s %s\n", cursor, name, cat))
	}

	if m.showDetail && m.cursor < len(filtered) {
		p := filtered[m.cursor]
		detail := fmt.Sprintf(
			"%s\n\n%s\n\n%s %s\n\n%s %s",
			titleStyle.Render(p.Name),
			p.Intent,
			categoryStyle.Render("When:"), p.When,
			categoryStyle.Render("Examples:"), p.Example,
		)
		b.WriteString("\n")
		b.WriteString(detailStyle.Render(detail))
	}

	b.WriteString("\n\n")
	b.WriteString(helpStyle.Render("j/k: navigate  enter: details  1-4: filter  q: quit"))

	return b.String()
}

func main() {
	m := model{patterns: patterns}
	p := tea.NewProgram(m, tea.WithAltScreen())
	if _, err := p.Run(); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}
}
