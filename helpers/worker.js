const { parentPort } = require('node:worker_threads');
const { Node } = require('../src/core/node.js');

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
    results.errors.push({ code: 'MISSING_ID', message: 'Node ID is required' });
  }
  if (!nodeInstance.type) {
    results.valid = false;
    results.errors.push({ code: 'MISSING_TYPE', message: 'Node type is required' });
  }

  await new Promise((resolve) => setTimeout(resolve, 10));
  return results;
}

parentPort.on('message', async ({ callbackId, action, payload }) => {
  try {
    switch (action) {
      case 'CREATE_NODE': {
        const node = new Node(payload.id, payload.type, payload.metadata);
        if (payload.attributes) {
          Object.entries(payload.attributes).forEach(([k, v]) => node.addAttribute(k, v));
        }
        parentPort.postMessage({ callbackId, success: true, node: node.toJSON() });
        break;
      }
      case 'VALIDATE_NODE': {
        const results = await validateNode(payload.node);
        parentPort.postMessage({ callbackId, success: true, results });
        break;
      }
      default:
        throw new Error(`Unknown action: ${action}`);
    }
  } catch (err) {
    parentPort.postMessage({ callbackId, success: false, error: err.message });
  }
});

parentPort.postMessage({ type: 'READY' });
