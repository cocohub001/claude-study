package handler

import (
	"net/http"

	"github.com/gateway/api-gateway/internal/model"
	"github.com/gateway/api-gateway/internal/service"
	"github.com/gin-gonic/gin"
)

type AdminHandler struct {
	service *service.RouteService
}

func NewAdminHandler(s *service.RouteService) *AdminHandler {
	return &AdminHandler{service: s}
}

func (h *AdminHandler) GetRoutes(c *gin.Context) {
	routes := h.service.GetAll()
	c.JSON(http.StatusOK, routes)
}

func (h *AdminHandler) AddRoute(c *gin.Context) {
	var route model.Route
	if err := c.ShouldBindJSON(&route); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	h.service.Add(&route)
	c.JSON(http.StatusCreated, route)
}

func (h *AdminHandler) RemoveRoute(c *gin.Context) {
	id := c.Param("id")
	h.service.Remove(id)
	c.Status(http.StatusNoContent)
}
