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
    if (!type || typeof type !== 'string') {
      throw new Error('Relationship type must be a non-empty string');
    }

    if (!target || typeof target !== 'string') {
      throw new Error('Relationship target must be a non-empty string');
    }

    const duplicate = this.relationships.some(
      (rel) => rel.type === type && rel.target === target
    );
    if (duplicate) {
      return this;
    }

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
   * Set or merge AI parameters on the node
   * @param {Object} parameters - AI parameters. Must be a plain object
   * @returns {Node} - The node instance for chaining
   */
  setAIParameters(parameters = {}) {
    if (
      typeof parameters !== 'object' ||
      parameters === null ||
      Array.isArray(parameters)
    ) {
      return this;
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
    if (!json || typeof json !== 'object') {
      throw new Error('Invalid JSON input for Node.fromJSON');
    }

    const id = json["@id"] || json.id;
    const type = json["@type"] || json.type;

    if (typeof id !== 'string' || typeof type !== 'string') {
      throw new Error('Node JSON must include string id and type');
    }

    const metadata = (typeof json.metadata === 'object' && json.metadata !== null) ? json.metadata : {};

    const node = new Node(
      id,
      type,
      metadata
    );

    const originalCreated = node.metadata.created;
    const originalModified = node.metadata.modified;
    
    // Restore attributes
    if (json.attributes && typeof json.attributes === 'object') {
      Object.entries(json.attributes).forEach(([key, value]) => {
        node.addAttribute(key, value);
      });
    }

    // Restore relationships
    if (Array.isArray(json.relationships)) {
      json.relationships.forEach(rel => {
        if (rel && typeof rel === 'object' && typeof rel.type === 'string' && typeof rel.target === 'string') {
          node.addRelationship(rel.type, rel.target, rel.metadata || {});
        }
      });
    }

    // Restore validation rules
    if (Array.isArray(json.validationRules)) {
      json.validationRules.forEach(rule => {
        if (rule && typeof rule === 'object') {
          node.addValidationRule(
            rule.ruleType,
            rule.expression,
            rule.severity,
            rule.message
          );
        }
      });
    }
    
    // Restore AI interface
    if (json.aiInterface && typeof json.aiInterface === 'object') {
      const ai = json.aiInterface;
      const params = (ai.parameters && typeof ai.parameters === 'object') ? ai.parameters : {};

      if (Array.isArray(ai.capabilities)) {
        ai.capabilities.forEach((capability, index) => {
          if (typeof capability === 'string') {
            node.addAICapability(capability, index === 0 ? params : {});
          }
        });
      } else if (Object.keys(params).length) {
        node.setAIParameters(params);
      }
    }
    
    // Restore extensions
    if (json.extensions && typeof json.extensions === 'object') {
      Object.entries(json.extensions).forEach(([namespace, data]) => {
        node.addExtension(namespace, data);
      });
    }

    if (originalCreated) node.metadata.created = originalCreated;
    if (originalModified) node.metadata.modified = originalModified;

    return node;
  }
}


// Export
if (typeof module !== 'undefined') {
  module.exports = { Node };
} else {
  self.Node = Node;
}

