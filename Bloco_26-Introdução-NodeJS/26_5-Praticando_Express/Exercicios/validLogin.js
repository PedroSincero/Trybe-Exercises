const express = require('express');

const validateEmail = (req, res, next) => {
  const { email } = req.body;
  const regex = /^[a-z0-9.]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$/i;
  if(!email || !email.match(regex)) return res.status(400).json({ message: 'Invalid Email'});

  next()
};

const validatePassword = (req, res, next) => {
  const { password } = req.body;

  if(
    typeof password === 'number' ||
      `${password}`.length <= 3 || 
      `${password}`.length >= 9
    ) return res.status(400).json({ message: 'Invalid Password'});
  next()
};

module.exports = { validatePassword, validateEmail };
