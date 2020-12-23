export default {
  /**
   * Loads an image from a given url
   * @param  {String}   url      url's of the image.
   * @return  {Promise} the loading image promise
   */
  loadImage: (url) => {
    return fetch(url)
      .then((response) => {
        return response.blob();
      })
      .then((blob) => {
        return new Promise((resolve, reject) => {
          const reader = new FileReader();
          reader.onloadend = () => {
            resolve(reader.result);
          };
          reader.onerror = reject;
          reader.readAsDataURL(blob);
        });
      });
  },
};
