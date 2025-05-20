// src/core/worker.node.js
/**
 * OpenPermit Worker - Node.js worker_threads implementation
 * Mirrors the logic of `worker.js` for Node environments.
 */

const { parentPort } = require('worker_threads');
const { Node } = require('./node.js');

/**
 * Validate a node against rules
 * @param {Object} node - Node to validate
 * @returns {Promise<Object>} - Validation results
 */
async function validateNode(node) {
  const nodeInstance = node instanceof Node ? node : Node.fromJSON(node);

  const results = {
    valid: true,
    errors: [],
    warnings: [],
    info: []
  };

  if (!nodeInstance.id) {
    results.valid = false;
    results.errors.push({
      code: 'MISSING_ID',
      message: 'Node ID is required'
    });
  }

  if (!nodeInstance.type) {
    results.valid = false;
    results.errors.push({
      code: 'MISSING_TYPE',
      message: 'Node type is required'
    });
  }

  await new Promise(resolve => setTimeout(resolve, 10));

  return results;
}

/**
 * Create a crosswalk between source and target nodes
 * @param {Object} source - Source node
 * @param {Object} target - Target node
 * @returns {Promise<Object>} - Created crosswalk
 */
async function createCrosswalk(source, target) {
  const crosswalk = {
    id: `crosswalk-${Date.now()}`,
    source: {
      nodeType: source.type,
      identifier: source.id
    },
    target: {
      nodeType: target.type,
      identifier: target.id
    },
    type: 'Standard-to-Standard',
    mappings: [],
    metadata: {
      creator: 'system',
      created: new Date().toISOString(),
      lastUpdated: new Date().toISOString(),
      status: 'draft',
      version: '1.0.0'
    },
    validationMethods: []
  };

  return crosswalk;
}

// Set up message handler for the worker
parentPort.on('message', async event => {
  const { action, payload, callbackId } = event;

  try {
    switch (action) {
      case 'CREATE_NODE': {
        const node = new Node(
          payload.id,
          payload.type,
          payload.metadata
        );

        if (payload.attributes) {
          Object.entries(payload.attributes).forEach(([key, value]) => {
            node.addAttribute(key, value);
          });
        }

        parentPort.postMessage({
          success: true,
          callbackId,
          node: node.toJSON()
        });
        break;
      }

      case 'VALIDATE_NODE': {
        const results = await validateNode(payload.node);
        parentPort.postMessage({
          success: true,
          callbackId,
          results
        });
        break;
      }

      case 'CREATE_CROSSWALK': {
        const crosswalk = await createCrosswalk(
          payload.source,
          payload.target
        );
        parentPort.postMessage({
          success: true,
          callbackId,
          crosswalk
        });
        break;
      }

      default:
        throw new Error(`Unknown action: ${action}`);
    }
  } catch (error) {
    parentPort.postMessage({
      success: false,
      callbackId,
      error: error.message
    });
  }
});

// Notify that the worker setup is complete
parentPort.postMessage({ type: 'ready' });

