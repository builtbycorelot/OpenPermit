// src/api/index.js
/**
 * OpenPermit API - Client interface for the OpenPermit framework
 * @module api
 */

/**
 * OpenPermit API client
 */
class OpenPermit {
  /**
   * Create a new OpenPermit client
   * @param {Object} options - Configuration options
   */
  constructor(options = {}) {
    this.options = {
      workerPath: './core/worker.js',
      ...options
    };
    
    this.worker = null;
    this.callbacks = new Map();
    this.callbackId = 0;
    this._readyResolve = null;
  }
  
  /**
   * Initialize the client
   * @returns {Promise<void>}
   */
  async init() {
    if (this.worker) return;
    
    // Prepare promise that resolves when the worker signals readiness
    const readyPromise = new Promise(resolve => {
      this._readyResolve = resolve;
    });

    // Create worker
    this.worker = new Worker(this.options.workerPath);

    // Set up message handler
    this.worker.addEventListener('message', event => {
      if (event.data && event.data.type === 'ready') {
        if (this._readyResolve) {
          this._readyResolve();
          this._readyResolve = null;
        }
        return;
      }

      const { callbackId, ...data } = event.data;

      if (callbackId && this.callbacks.has(callbackId)) {
        const { resolve, reject } = this.callbacks.get(callbackId);

        if (data.success) {
          resolve(data);
        } else {
          reject(new Error(data.error || 'Unknown error'));
        }

        this.callbacks.delete(callbackId);
      }
    });

    // Wait for worker to signal it is ready
    await readyPromise;
  }
  
  /**
   * Send a message to the worker
   * @param {string} action - Action to perform
   * @param {Object} payload - Action payload
   * @returns {Promise<Object>} - Response from worker
   */
  async sendMessage(action, payload = {}) {
    await this.init();
    
    return new Promise((resolve, reject) => {
      const callbackId = ++this.callbackId;
      
      this.callbacks.set(callbackId, { resolve, reject });
      
      this.worker.postMessage({
        callbackId,
        action,
        payload
      });
    });
  }
  
  /**
   * Create a new node
   * @param {Object} options - Node options
   * @returns {Promise<Object>} - Created node
   */
  async createNode(options) {
    const response = await this.sendMessage('CREATE_NODE', options);
    return response.node;
  }
  
  /**
   * Validate a node
   * @param {Object} node - Node to validate
   * @returns {Promise<Object>} - Validation results
   */
  async validateNode(node) {
    const response = await this.sendMessage('VALIDATE_NODE', { node });
    return response.results;
  }
  
  /**
   * Create a crosswalk between source and target nodes
   * @param {Object} source - Source node
   * @param {Object} target - Target node
   * @returns {Promise<Object>} - Created crosswalk
   */
  async createCrosswalk(source, target) {
    const response = await this.sendMessage('CREATE_CROSSWALK', { source, target });
    return response.crosswalk;
  }
}

// Export for browser and Node.js environments
if (typeof window !== 'undefined') {
  window.OpenPermit = OpenPermit;
} else if (typeof module !== 'undefined') {
  module.exports = { OpenPermit };
}

