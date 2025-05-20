(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    // Node environment
    factory(require('chai'), require('../src/api/index.js'));
  } else {
    // Browser environment
    root.openPermitTests = function() {
      factory(root.chai, root.OpenPermit);
    };
  }
}(this, function(chai, OpenPermitModule) {
  var expect = chai.expect;
  var OpenPermit = OpenPermitModule.OpenPermit || OpenPermitModule;

  describe('OpenPermit API', function() {
    this.timeout(5000);

    it('creates and validates a node', async function() {
      var client = new OpenPermit({ workerPath: '../src/core/worker.js' });
      await client.init();
      var node = await client.createNode({ id: 'test-node', type: 'TestNode' });
      var results = await client.validateNode(node);
      expect(results).to.be.an('object');
      expect(results.valid).to.equal(true);
    });
  });
}));
