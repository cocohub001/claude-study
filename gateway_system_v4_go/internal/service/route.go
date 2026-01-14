package service

import (
	"sync"

	"github.com/gateway/api-gateway/internal/model"
)

type RouteService struct {
	routes map[string]*model.Route
	mu     sync.RWMutex
}

func NewRouteService() *RouteService {
	return &RouteService{
		routes: make(map[string]*model.Route),
	}
}

func (s *RouteService) GetAll() []*model.Route {
	s.mu.RLock()
	defer s.mu.RUnlock()

	result := make([]*model.Route, 0, len(s.routes))
	for _, r := range s.routes {
		result = append(result, r)
	}
	return result
}

func (s *RouteService) Get(id string) *model.Route {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.routes[id]
}

func (s *RouteService) Add(route *model.Route) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.routes[route.ID] = route
}

func (s *RouteService) Remove(id string) {
	s.mu.Lock()
	defer s.mu.Unlock()
	delete(s.routes, id)
}

func (s *RouteService) FindByPath(path string) *model.Route {
	s.mu.RLock()
	defer s.mu.RUnlock()

	for _, r := range s.routes {
		if r.Enabled && len(path) >= len(r.Path) && path[:len(r.Path)] == r.Path {
			return r
		}
	}
	return nil
}
