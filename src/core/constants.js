// src/core/constants.js
/**
 * OpenPermit Constants
 * @module core/constants
 */

/**
 * Node types
 * @enum {string}
 */
const NODE_TYPES = {
  STANDARD: 'StandardNode',
  COMPONENT: 'ComponentNode',
  REQUIREMENT: 'RequirementNode',
  PROPERTY: 'PropertyNode',
  PROCESS: 'ProcessNode',
  ACTOR: 'ActorNode',
  DOCUMENT: 'DocumentNode',
  VALIDATION: 'ValidationNode'
};

/**
 * Relationship types
 * @enum {string}
 */
const RELATIONSHIP_TYPES = {
  IMPLEMENTS: 'implements',
  REFERENCES: 'references',
  CONTAINS: 'contains',
  VALIDATES: 'validates',
  REQUIRES: 'requires',
  EQUIVALENT: 'equivalent',
  DERIVES: 'derives',
  CONNECTS: 'connects'
};

/**
 * Validation rule types
 * @enum {string}
 */
const VALIDATION_RULE_TYPES = {
  REQUIREMENT: 'requirement',
  CONSTRAINT: 'constraint',
  CONSISTENCY: 'consistency',
  FORMAT: 'format',
  REFERENCE: 'reference'
};

/**
 * Severity levels
 * @enum {string}
 */
const SEVERITY_LEVELS = {
  ERROR: 'error',
  WARNING: 'warning',
  INFO: 'info',
  HINT: 'hint'
};

/**
 * AI capabilities
 * @enum {string}
 */
const AI_CAPABILITIES = {
  VALIDATION: 'validation',
  RECOMMENDATION: 'recommendation',
  EXPLANATION: 'explanation',
  INFERENCE: 'inference',
  CONFLICT_RESOLUTION: 'conflictResolution',
  UNCERTAINTY: 'uncertaintyManagement',
  LEARNING: 'continuousLearning'
};

if (typeof module !== 'undefined') {
  module.exports = {
    NODE_TYPES,
    RELATIONSHIP_TYPES,
    VALIDATION_RULE_TYPES,
    SEVERITY_LEVELS,
    AI_CAPABILITIES
  };
} else {
  self.NODE_TYPES = NODE_TYPES;
  self.RELATIONSHIP_TYPES = RELATIONSHIP_TYPES;
  self.VALIDATION_RULE_TYPES = VALIDATION_RULE_TYPES;
  self.SEVERITY_LEVELS = SEVERITY_LEVELS;
  self.AI_CAPABILITIES = AI_CAPABILITIES;
}

