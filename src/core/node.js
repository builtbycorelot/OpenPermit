// src/core/node.js
/**
 * OpenPermit Node - Core implementation of self-defining node structure
 * @module core/node
 */

/**
 * Node class representing a self-defining node in the ontology
 */
class Node {
  /**
   * Create a new node
   * @param {string} id - Unique node identifier (URI)
   * @param {string} type - Node type identifier
   * @param {Object} metadata - Node metadata
   */
  constructor(id, type, metadata = {}) {
    this.id = id;
    this.type = type;
    this.metadata = {
      name: '',
      description: '',
      version: '1.0.0',
      created: new Date().toISOString(),
      modified: new Date().toISOString(),
      ...metadata
    };
    this.attributes = {};
    this.relationships = [];
    this.validationRules = [];
    this.aiInterface = {
      capabilities: [],
      parameters: {}
    };
    this.extensions = {};
  }

  /**
   * Add an attribute to the node
   * @param {string} key - Attribute key
   * @param {any} value - Attribute value
   * @returns {Node} - The node instance for chaining
   */
  addAttribute(key, value) {
    this.attributes[key] = value;
    this.metadata.modified = new Date().toISOString();
    return this;
  }

  /**
   * Add a relationship to the node
   * @param {string} type - Relationship type
   * @param {string} target - Target node URI
   * @param {Object} metadata - Relationship metadata
   * @returns {Node} - The node instance for chaining
   */
  addRelationship(type, target, metadata = {}) {
    this.relationships.push({
      type,
      target,
      metadata
    });
    this.metadata.modified = new Date().toISOString();
    return this;
  }

  /**
   * Add a validation rule to the node
   * @param {string} ruleType - Type of validation rule
   * @param {string} expression - Rule expression
   * @param {string} severity - Severity level
   * @param {string} message - Human-readable message
   * @returns {Node} - The node instance for chaining
   */
  addValidationRule(ruleType, expression, severity = 'error', message = '') {
    this.validationRules.push({
      ruleType,
      expression,
      severity,
      message
    });
    this.metadata.modified = new Date().toISOString();
    return this;
  }

  /**
   * Add AI capability to the node
   * @param {string} capability - AI capability identifier
   * @param {Object} parameters - AI parameters
   * @returns {Node} - The node instance for chaining
   */
  addAICapability(capability, parameters = {}) {
    if (!this.aiInterface.capabilities.includes(capability)) {
      this.aiInterface.capabilities.push(capability);
    }
    
    this.aiInterface.parameters = {
      ...this.aiInterface.parameters,
      ...parameters
    };
    
    this.metadata.modified = new Date().toISOString();
    return this;
  }

  /**
   * Add extension data to the node
   * @param {string} namespace - Extension namespace
   * @param {Object} data - Extension data
   * @returns {Node} - The node instance for chaining
   */
  addExtension(namespace, data) {
    this.extensions[namespace] = data;
    this.metadata.modified = new Date().toISOString();
    return this;
  }

  /**
   * Convert node to JSON representation
   * @returns {Object} - JSON representation of the node
   */
  toJSON() {
    return {
      "@context": "https://openpermit.org/schemas/node/v1",
      "@id": this.id,
      "@type": this.type,
      "metadata": this.metadata,
      "attributes": this.attributes,
      "relationships": this.relationships,
      "validationRules": this.validationRules,
      "aiInterface": this.aiInterface,
      "extensions": this.extensions
    };
  }

  /**
   * Create a node from JSON representation
   * @param {Object} json - JSON representation of the node
   * @returns {Node} - New node instance
   */
  static fromJSON(json) {
    const node = new Node(
      json["@id"] || json.id,
      json["@type"] || json.type,
      json.metadata || {}
    );
    
    // Restore attributes
    if (json.attributes) {
      Object.entries(json.attributes).forEach(([key, value]) => {
        node.addAttribute(key, value);
      });
    }
    
    // Restore relationships
    if (json.relationships) {
      json.relationships.forEach(rel => {
        node.addRelationship(rel.type, rel.target, rel.metadata || {});
      });
    }
    
    // Restore validation rules
    if (json.validationRules) {
      json.validationRules.forEach(rule => {
        node.addValidationRule(
          rule.ruleType,
          rule.expression,
          rule.severity,
          rule.message
        );
      });
    }
    
    // Restore AI interface
    if (json.aiInterface) {
      if (json.aiInterface.capabilities) {
        json.aiInterface.capabilities.forEach(capability => {
          node.addAICapability(capability);
        });
      }
      
      if (json.aiInterface.parameters) {
        Object.entries(json.aiInterface.parameters).forEach(([key, value]) => {
          node.aiInterface.parameters[key] = value;
        });
      }
    }
    
    // Restore extensions
    if (json.extensions) {
      Object.entries(json.extensions).forEach(([namespace, data]) => {
        node.addExtension(namespace, data);
      });
    }
    
    return node;
  }
}
