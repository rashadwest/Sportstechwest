# n8n Quick Debugging Reference

## 🚨 Common Errors & Quick Fixes

### Error: "bash: not found"
**Fix:** Change command from `bash` to `/bin/sh`

### Error: "Variable not found" or empty values
**Fix:** 
1. Use Code node to access: `$env.VARIABLE_NAME`
2. Pass through workflow: `$json.variable`
3. Make node conditional if variable optional

### Error: "Template variables not expanding"
**Fix:** Enable Expression Mode: `={{ `text ${$json.var}` }}`

### Error: "Workflow stuck on node"
**Fix:** Make node conditional, add skip logic

## ✅ Best Practices Checklist

- [ ] Use `/bin/sh` not `bash`
- [ ] Enable Expression Mode for variables
- [ ] Make critical nodes conditional
- [ ] Test each node before adding next
- [ ] Add fallback values: `|| 'default'`
- [ ] Never let one node block workflow
- [ ] Use Code nodes for complex logic
- [ ] Pass variables through workflow

## 🔧 Node Type Guide

- **Code Node:** Logic, data access, transformations
- **Execute Command:** Shell commands (use `/bin/sh`)
- **IF Node:** Conditional logic, error handling
- **HTTP Request:** API calls, webhooks

## 📋 Debugging Steps

1. Check node input data
2. Verify node configuration  
3. Test node in isolation
4. Check environment variables
5. Add conditional logic if needed
