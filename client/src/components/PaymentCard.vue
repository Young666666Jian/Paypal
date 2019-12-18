<template>
  <v-card flat>
    <paypal
      class="py-3"
      env="sandbox"
      amount="10"
      currency="USD"
      locale="en_US"
      :client="credentials"
      :items="transactions"
      v-on:payment-authorized="paymentauthorized"
      v-on:payment-completed="paymentcompleted"
      v-on:payment-cancelled="cancel"
    />
    <div id="paypal-button-container"></div>
  </v-card>
</template>
<script>
// import paypal from 'paypal-checkout';
import paypal from "vue-paypal-checkout";
export default {
  components: {
    paypal
  },
  data() {
    return {
      credentials: {
        sandbox:
          "AYt31Z0myIBIQFgluo0_MmIg9sbIhNgig7B7CL7iLXwPKeK9CMPyl1jsesT025Bm_rGHnpKTgaoyRLwM",
        production: ""
      },
      axiosConfig: {
        auth: {
          username:
            "AZR_Yl5jxWQrdb7GZoou948U9mafv1j9icVzZyrDzC-6J6c1JPGmx7LdQ-hhqg5WeMgx8NkaBwyo0ygW",
          password:
            "EGR5NebL3_PPrWuK8zvn8xAZMwpjudavdqS8NW3P-OsBClF3Cm0KexjHNgpZzKvbAb3W8iSF7aRBXAE1"
        }
      },
      transactions: [
        {
          "name": "hat",
          "description": "Brown hat.",
          "quantity": "1",
          "price": "5",
          "currency": "USD"
          },
          {
          "name": "handbag",
          "description": "Black handbag.",
          "quantity": "1",
          "price": "5",
          "currency": "USD"
          }
      ]
    };
  },
  mounted() {},
  created() {},
  methods: {
    paymentauthorized(response) {
      //remove ID prefix
      const orderId = response.orderID
      const index = orderId.indexOf("-");
      response.orderID = orderId.substring(index + 1);
      this.$http.post("/api/v1/paypal/order", {
        response,
        transactions: this.transactions
      });
    },
    cancel() {
      console.log("hehehehhehehe");
    },
    paymentcompleted(response) {
      console.log(JSON.stringify(response));
    }
  }
};
</script>
>
