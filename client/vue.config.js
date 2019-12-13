module.exports = {
  css: {
    loaderOptions: {
      sass: {
        prependData: '@import "~@/sass/main.scss"'
      }
    }
  },
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000"
      },
      "/napi": {
        target: "ws://localhost:5000",
        ws: true
      }
    }
  },
  transpileDependencies: ["vuetify"]
};
