/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './website/templates/**/*.html',
    './website/**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        'light-gray': '#D9D9D9',
        'light-orange': '#FFB86C',
        'dark-orange': '#FF9F4A',
      },
    },
  },
  plugins: [],
}
