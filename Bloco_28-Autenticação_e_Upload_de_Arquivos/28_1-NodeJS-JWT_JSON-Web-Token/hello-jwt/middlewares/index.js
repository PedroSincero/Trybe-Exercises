// middlewares/index.js

const auth = require('./auth');
const error = require('./error');
const admin = require('./admin');

module.exports = {
  auth,
  error,
  admin,
};