import * as Yup from 'yup';
import Product from '../models/Product';

class ProductDetailController {
  async index(req, res) {
    const { id } = req.params;

    const product = await Product.findOne({
      where: { id },
      attributes: ['id', 'name', 'description', 'price', 'stock'],
    });

    return res.json(product);
  }

  async update(req, res) {
    const schema = Yup.object().shape({
      name: Yup.string().notRequired(),
      description: Yup.string().notRequired(),
      price: Yup.number(),
      stock: Yup.number(),
    });

    if (!(await schema.isValid(req.body))) {
      return res.status(400).json({ error: 'Invalid body request.' });
    }

    const { id } = req.params;

    const product = await Product.findByPk(id);

    const updated_product = await product.update(req.body);

    return res.json(updated_product);
  }

  async delete(req, res) {
    const { id } = req.params;

    const product = await Product.findByPk(id);

    await product.destroy();

    return res.status(204).json();
  }
}

export default new ProductDetailController();
