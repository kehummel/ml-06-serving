Practice requests used to test server and warning messages. Only formatted for windows.

### Initial: Not diabetic
curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 117, "BMI": 32, "age": 29}'

### Diabetic
curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 150, "BMI": 32, "age": 55}'

### not diabetic, but lower probability
curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 130, "BMI": 29, "age": 35}'

### Diabetic with 62.5 % probability
curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 130, "BMI": 32, "age": 35}'

### Missing Features
curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 117}'

### low glucose warning
curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 60, "BMI": 29, "age": 29}'

### low BMI warning
curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 117, "BMI": 11, "age": 29}'

### High BMI warning
curl -X POST http://127.0.0.1:8000/predict `
         -H "Content-Type: application/json" `
         -d '{"glucose": 117, "BMI": 52, "age": 29}'
