package model

type Route struct {
	ID      string   `json:"id"`
	Path    string   `json:"path"`
	Backend string   `json:"backend"`
	Methods []string `json:"methods"`
	Enabled bool     `json:"enabled"`
}
