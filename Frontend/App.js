import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Box,
  Container,
  Typography,
  TextField,
  Button,
  CircularProgress,
  Paper,
  AppBar,
  Toolbar,
  IconButton,
  Autocomplete,
  Fade,
  Slide,
  useMediaQuery,
  CssBaseline
} from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Brightness4, Brightness7, ShowChart, TrendingUp, Assessment } from '@mui/icons-material';

function App() {
  const [stocks, setStocks] = useState([]);
  const [selectedStock, setSelectedStock] = useState(null);
  const [inputValue, setInputValue] = useState('');
  const [inference, setInference] = useState('');
  const [timestamp, setTimestamp] = useState('');
  const [loading, setLoading] = useState(false);
  const [fetchingStocks, setFetchingStocks] = useState(true);
  const [error, setError] = useState('');
  const [showMainContent, setShowMainContent] = useState(false);
  const [darkMode, setDarkMode] = useState(false);

  const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');

  const theme = createTheme({
    palette: {
      mode: darkMode ? 'dark' : 'light',
      primary: {
        main: '#1976d2',
      },
      background: {
        default: darkMode ? '#121212' : '#f5f9ff',
        paper: darkMode ? '#1e1e1e' : '#ffffff'
      },
      text: {
        primary: darkMode ? '#e0e0e0' : '#212121'
      }
    },
    typography: {
      fontFamily: 'Inter, sans-serif'
    }
  });

  useEffect(() => {
    fetchStocks();
    const timer = setTimeout(() => setShowMainContent(true), 500);
    return () => clearTimeout(timer);
  }, []);

  const fetchStocks = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/stocks');
      setStocks(response.data.stocks);
    } catch (error) {
      setError('Failed to fetch stocks.');
    } finally {
      setFetchingStocks(false);
    }
  };

  const handleInference = async () => {
    if (!selectedStock) {
      setError('Please select a stock.');
      return;
    }

    setLoading(true);
    setError('');
    setInference('');
    setTimestamp('');

    try {
      const response = await axios.get(
        `http://localhost:8000/get_inference/?company=${encodeURIComponent(selectedStock)}`
      );
      setInference(response.data['MODEL RESPONSE']);
      setTimestamp(response.data['timestamp']);
    } catch (error) {
      setError(error.response?.data?.detail || 'Failed to get inference.');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setSelectedStock(null);
    setInputValue('');
    setInference('');
    setTimestamp('');
    setError('');
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppBar position="sticky" color="default" elevation={1}>
        <Toolbar sx={{ justifyContent: 'space-between' }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <TrendingUp color="primary" />
            <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
              NiveshAI
            </Typography>
          </Box>
          <IconButton onClick={() => setDarkMode(!darkMode)} color="inherit">
            {darkMode ? <Brightness7 /> : <Brightness4 />}
          </IconButton>
        </Toolbar>
      </AppBar>

      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          minHeight: '40vh',
          flexDirection: 'column',
          textAlign: 'center',
          px: 2
        }}
      >
        <Box sx={{ mb: 3, display: 'flex', gap: 2 }}>
          <Assessment sx={{ fontSize: 40, color: 'primary.main' }} />
          <ShowChart sx={{ fontSize: 40, color: 'primary.main' }} />
          <TrendingUp sx={{ fontSize: 40, color: 'primary.main' }} />
        </Box>
        <Typography variant="h3" fontWeight={700} color="primary" gutterBottom>
          Welcome to NiveshAI
        </Typography>
        <Typography variant="h6" color="text.secondary">
          Expert AI insights for your portfolio
        </Typography>
      </Box>

      <Box sx={{ py: 6, backgroundColor: 'background.default' }}>
        <Container maxWidth="md">
          <Slide in={showMainContent} direction="up" timeout={800}>
            <Box>
              <Typography variant="h4" fontWeight={700} color="primary" align="center" mb={4}>
                Select Your Stock
              </Typography>

              <Paper elevation={3} sx={{ p: 4, mb: 4, borderRadius: 3 }}>
                <Autocomplete
                  options={stocks}
                  loading={fetchingStocks}
                  renderInput={(params) => (
                    <TextField
                      {...params}
                      label="Choose a company"
                      variant="outlined"
                      error={!!error}
                      helperText={error}
                      fullWidth
                      InputProps={{
                        ...params.InputProps,
                        endAdornment: (
                          <>
                            {fetchingStocks && <CircularProgress color="inherit" size={20} />}
                            {params.InputProps.endAdornment}
                          </>
                        )
                      }}
                    />
                  )}
                  value={selectedStock}
                  onChange={(event, newValue) => {
                    setSelectedStock(newValue);
                    setError('');
                  }}
                  inputValue={inputValue}
                  onInputChange={(event, newInputValue) => {
                    setInputValue(newInputValue);
                  }}
                  fullWidth
                  freeSolo
                />

                <Button
                  variant="contained"
                  fullWidth
                  size="large"
                  onClick={handleInference}
                  disabled={loading || !selectedStock}
                  sx={{ mt: 3 }}
                >
                  {loading ? 'Analyzing...' : 'Get AI Analysis'}
                </Button>

                {inference && (
                  <Button
                    variant="text"
                    onClick={handleReset}
                    fullWidth
                    sx={{ mt: 2, color: 'primary.main' }}
                  >
                    Reset
                  </Button>
                )}
              </Paper>

              {loading && (
                <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
                  <CircularProgress size={60} color="primary" />
                </Box>
              )}

              {inference && (
                <Fade in timeout={600}>
                  <Paper
                    elevation={4}
                    sx={{
                      p: 4,
                      borderRadius: 3,
                      backgroundColor: 'background.paper',
                      boxShadow: 3
                    }}
                  >
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                      <Typography variant="h5" fontWeight="bold" color="primary">
                        AI Analysis
                      </Typography>
                      {timestamp && (
                        <Typography variant="caption" color="text.secondary">
                          {timestamp}
                        </Typography>
                      )}
                    </Box>

                    <Box sx={{ whiteSpace: 'pre-line', fontSize: '1.1rem', lineHeight: 1.7 }}>
                      {inference.split('\n').map((line, index) => {
                        const headingMatch = line.match(/^__\*\*(.*?)\*\*__$/);
                        if (headingMatch) {
                          return (
                            <Typography
                              key={index}
                              sx={{
                                color: 'primary.main',
                                fontWeight: 'bold',
                                textDecoration: 'underline',
                                mt: 3
                              }}
                            >
                              {headingMatch[1]}
                            </Typography>
                          );
                        }

                        const riskMatch = line.match(/^(Low Risk:|Medium Risk:|High Risk:)/);
                        if (riskMatch) {
                          return (
                            <Typography key={index} sx={{ mt: 2 }}>
                              <span style={{ textDecoration: 'underline', fontWeight: 600 }}>
                                {riskMatch[1]}
                              </span>
                              {line.replace(riskMatch[1], '')}
                            </Typography>
                          );
                        }

                        return (
                          <Typography key={index} sx={{ mb: 1 }}>
                            {line}
                          </Typography>
                        );
                      })}
                    </Box>
                  </Paper>
                </Fade>
              )}
            </Box>
          </Slide>
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App;
