/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#5DBAAA',
          dark: '#4A9A8C',
          light: '#7DCDBF',
        },
        secondary: {
          DEFAULT: '#1E3A5F',
          light: '#2E4A6F',
        },
        accent: {
          red: '#EF4444',
          orange: '#F97316',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
