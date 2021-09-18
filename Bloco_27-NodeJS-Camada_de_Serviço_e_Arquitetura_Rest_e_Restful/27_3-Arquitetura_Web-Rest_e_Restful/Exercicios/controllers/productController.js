const express = require('express');
const ProductModel = require('../models/productModel');

const router = express.Router();
const MESSAGE_PRODUCT = {message: 'Product not found'};

router.get('/', async (req, res, next) => {
  const products = await ProductModel.getAll();

  if(!products) return res.status(404).json(MESSAGE_PRODUCT);
  res.status(200).json(products);
});

router.get('/:id', async (req, res, next) => {
  const product = await ProductModel.getById(req.params.id);

  if(!product) return res.status(404).json(MESSAGE_PRODUCT);
  res.status(200).json(product);
});

router.post('/', async (req, res) => {
  const { name, brand } = req.body;

  const newProduct = await ProductModel.add(name, brand);

  if(!newProduct) return res.status(404).json({message: 'error while updating'});
  
  res.status(200).json(newProduct);
});

router.delete('/:id', async (req, res) => {
  const products = await ProductModel.exclude(req.params.id);

  if(!products) return res.status(404).json({message: 'error deleting product, id invalid'});

  res.status(200).json(products);
});

router.put('/:id', async (req, res) => {
  const { name, brand } = req.body;

  const products = await ProductModel.update(req.params.id, name, brand);

  if(!products) return res.status(404).json({message: 'error editing product'});

  res.status(200).json(products);
});

module.exports = router;
