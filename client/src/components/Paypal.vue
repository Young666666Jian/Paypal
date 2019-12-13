<template>
  <div :id="id" class="paypal-button"></div>
</template>
<script>
import paypal from "paypal-checkout";
export default {
  props: {
    amount: {
      type: Number,
      default: 0
    },
    currency: {
      type: String,
      default: "USD"
    },
    details: {
      type: Object,
      default: {}
    }
  },
  methods: {
    payment() {
      const vue = this;
      const transaction = {
        amount: {
          total: this.amount,
          currency: this.currency,
          details: this.details
        }
      };
      const payment = {
        transactions: [transaction]
      };
      return paypal.rest.payment.create(this.env, this.client, payment);
    },
    onAuthorize(data, actions) {},
    onCancel(data) {}
  },
  mounted() {
    const vue = this;
    const button = Object.assign(
      {
        // Pass in env
        env: vue.env,
        // Pass in the client ids to use to create your transaction
        // on sandbox and production environments
        client: vue.client,
        // Pass the payment details for your transaction
        // See https://developer.paypal.com/docs/api/payments/#payment_create for the expected json parameters
        payment: vue.payment,
        // Display a "Pay Now" button rather than a "Continue" button
        commit: vue.commit,
        // Pass a function to be called when the customer completes the payment
        onAuthorize: vue.onAuthorize,
        // Pass a function to be called when the customer cancels the payment
        onCancel: vue.onCancel
      },
      assignTo(vue, propTypes.BUTTON)
    );
    paypal.Button.render(button, vue.$el);
  }
};
</script>
>
