import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
      light: '#42a5f5',
      dark: '#1565c0',
      contrastText: '#ffffff'
    },
    secondary: {
      main: '#e3f2fd',
      light: '#f5f9ff',
      dark: '#bbdefb',
      contrastText: '#1976d2'
    },
    background: {
      default: '#ffffff',
      paper: '#ffffff'
    },
    text: {
      primary: '#1976d2',
      secondary: '#424242'
    }
  },
  typography: {
    fontFamily: [
      'Inter',
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif'
    ].join(','),
    h1: {
      fontWeight: 700,
      color: '#1976d2'
    },
    h2: {
      fontWeight: 700,
      color: '#1976d2'
    },
    h3: {
      fontWeight: 600,
      color: '#1976d2'
    },
    h4: {
      fontWeight: 600,
      color: '#1976d2'
    },
    h5: {
      fontWeight: 600,
      color: '#1976d2'
    },
    h6: {
      fontWeight: 600,
      color: '#1976d2'
    },
    body1: {
      color: '#424242',
      lineHeight: 1.6
    },
    body2: {
      color: '#424242',
      lineHeight: 1.6
    }
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
          fontWeight: 600,
          borderRadius: 8,
          padding: '10px 24px',
          transition: 'all 0.3s ease'
        },
        contained: {
          boxShadow: '0 4px 15px rgba(25, 118, 210, 0.3)',
          '&:hover': {
            boxShadow: '0 6px 20px rgba(25, 118, 210, 0.4)',
            transform: 'translateY(-2px)'
          }
        }
      }
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          boxShadow: '0 4px 20px rgba(25, 118, 210, 0.08)'
        }
      }
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          '& .MuiOutlinedInput-root': {
            borderRadius: 8,
            transition: 'all 0.3s ease',
            '&:hover': {
              boxShadow: '0 2px 8px rgba(25, 118, 210, 0.1)'
            },
            '&.Mui-focused': {
              boxShadow: '0 2px 12px rgba(25, 118, 210, 0.2)'
            }
          }
        }
      }
    },
    MuiAutocomplete: {
      styleOverrides: {
        listbox: {
          '& .MuiAutocomplete-option': {
            color: '#1976d2',
            '&:hover': {
              backgroundColor: '#f5f9ff'
            },
            '&.Mui-focused': {
              backgroundColor: '#e3f2fd'
            }
          }
        }
      }
    }
  }
});

export default theme;