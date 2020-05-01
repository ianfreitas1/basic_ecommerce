import * as Yup from 'yup';
import Product from '../models/Product';

class ProductController {
  async index(req, res) {
    const products = await Product.findAll();

    return res.json(products);
  }

  async store(req, res) {
    const schema = Yup.object().shape({
      name: Yup.string().required(),
      description: Yup.string().required(),
      price: Yup.number().required(),
      stock: Yup.number().required(),
    });

    if (!(await schema.isValid(req.body))) {
      return res.status(400).json({ message: 'Invalid body request.' });
    }

    const { name, description, price, stock } = req.body;

    const product = await Product.create({
      name,
      description,
      price,
      stock,
    });

    return res.status(201).json(product);
  }
}

export default new ProductController();
