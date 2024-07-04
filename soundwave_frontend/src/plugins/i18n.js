import { createI18n } from 'vue-i18n';

const messages = {
    'en': {
        welcomeMsg:'Welcome to Soundwave !',
        language: 'Language'
    },
    'fr': {
        welcomeMsg:'Bienvenue sur Soundwave !',
        language: 'Langue'
    },
    'de': {
        welcomeMsg:'Wilkommen ... Soundwave !',
        language: 'Sprache'
    },
    'nl': {
        welcomeMsg: 'Welkom ... Soundwave !',
        language: 'Taal'
    },
}

// eslint-disable-next-line
const i18n =  createI18n({
    locale: 'en', // set locale
    fallbackLocale: 'en', // set fallback locale
    messages, // set locale messages
});

export default i18n;