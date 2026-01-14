package main

import (
	"github.com/gateway/api-gateway/internal/handler"
	"github.com/gateway/api-gateway/internal/service"
	"github.com/gin-gonic/gin"
)

func main() {
	routeService := service.NewRouteService()
	adminHandler := handler.NewAdminHandler(routeService)
	gatewayHandler := handler.NewGatewayHandler(routeService)

	r := gin.Default()

	// Health endpoint
	r.GET("/health", func(c *gin.Context) {
		c.JSON(200, gin.H{"status": "healthy"})
	})

	// Admin routes
	admin := r.Group("/admin")
	{
		admin.GET("/routes", adminHandler.GetRoutes)
		admin.POST("/routes", adminHandler.AddRoute)
		admin.DELETE("/routes/:id", adminHandler.RemoveRoute)
	}

	// Gateway proxy
	r.NoRoute(gatewayHandler.Proxy)

	r.Run(":8080")
}
