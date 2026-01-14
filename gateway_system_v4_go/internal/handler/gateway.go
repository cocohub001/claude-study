package handler

import (
	"io"
	"net/http"

	"github.com/gateway/api-gateway/internal/service"
	"github.com/gin-gonic/gin"
)

type GatewayHandler struct {
	service *service.RouteService
	client  *http.Client
}

func NewGatewayHandler(s *service.RouteService) *GatewayHandler {
	return &GatewayHandler{
		service: s,
		client:  &http.Client{},
	}
}

func (h *GatewayHandler) Proxy(c *gin.Context) {
	path := c.Request.URL.Path
	route := h.service.FindByPath(path)

	if route == nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "route not found"})
		return
	}

	targetURL := route.Backend + path
	req, err := http.NewRequest(c.Request.Method, targetURL, c.Request.Body)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	resp, err := h.client.Do(req)
	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{"error": err.Error()})
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	c.Data(resp.StatusCode, resp.Header.Get("Content-Type"), body)
}
