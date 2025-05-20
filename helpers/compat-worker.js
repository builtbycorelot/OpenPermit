const { Worker: NodeWorker } = require('node:worker_threads');

class CompatWorker extends NodeWorker {
  constructor(filename, options) {
    super(filename, options);
    this._listeners = new Map();
  }

  addEventListener(event, listener) {
    const wrapper = (data) => listener({ data });
    this._listeners.set(listener, wrapper);
    this.on(event, wrapper);
  }

  removeEventListener(event, listener) {
    const wrapper = this._listeners.get(listener);
    if (wrapper) {
      this.off(event, wrapper);
      this._listeners.delete(listener);
    }
  }
}

module.exports = CompatWorker;
