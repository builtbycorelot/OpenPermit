const test = require('node:test');
const assert = require('node:assert');
const { Node } = require('../src/core/node.js');

test('Node toJSON/fromJSON round trip', (t) => {
  const node = new Node('id1', 'StandardNode', { name: 'Test Node' });
  node.addAttribute('foo', 'bar');
  const json = node.toJSON();
  const clone = Node.fromJSON(json);
  assert.deepStrictEqual(clone.toJSON(), json);
});
