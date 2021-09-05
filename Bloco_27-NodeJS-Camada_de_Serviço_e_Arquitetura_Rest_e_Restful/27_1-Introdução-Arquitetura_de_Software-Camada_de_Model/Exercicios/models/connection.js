const { MongoClient } = require('mongodb');

const OPTIONS = {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}

const MONGO_DB_URL = 'mongodb://127.0.0.1:27017';

let db = null;

const connection = async () => {
  if (!db) {
    const conn = await MongoClient.connect(MONGO_DB_URL, OPTIONS);
    db = conn.db('model_example');
    return db;
  }
  return Promise.resolve(db);
};
module.exports = connection;
