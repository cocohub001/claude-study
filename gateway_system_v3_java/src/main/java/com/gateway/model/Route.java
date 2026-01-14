package com.gateway.model;

import java.util.List;

public class Route {
    private String id;
    private String path;
    private String backend;
    private List<String> methods;
    private boolean enabled;

    public Route() {}

    public Route(String id, String path, String backend,
                 List<String> methods, boolean enabled) {
        this.id = id;
        this.path = path;
        this.backend = backend;
        this.methods = methods;
        this.enabled = enabled;
    }

    // Getters and Setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getPath() { return path; }
    public void setPath(String path) { this.path = path; }

    public String getBackend() { return backend; }
    public void setBackend(String backend) { this.backend = backend; }

    public List<String> getMethods() { return methods; }
    public void setMethods(List<String> methods) { this.methods = methods; }

    public boolean isEnabled() { return enabled; }
    public void setEnabled(boolean enabled) { this.enabled = enabled; }
}
