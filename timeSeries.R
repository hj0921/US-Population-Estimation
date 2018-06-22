library(xts)
library(forecast)
library(tidyverse)

data = read.csv('data_table.csv')
data = data %>% select(-X)
data_asian <- data %>% filter(raceID == 31)
data_black <- data%>% filter(raceID == 5)
data_hispanic <- data%>% filter(raceID == 400)
data_white <- data%>% filter(raceID == 3)
data_total <- data%>% filter(raceID == 1)

df <- data.frame(under18=integer(),
                 age18to34=integer(), 
                 age35to64=integer(),
                 age65plus=integer(),
                 state=character(),
                 raceID=integer(),
                 totalPopulation=integer(),
                 year=integer(),
                 stringsAsFactors=FALSE)

# asian
data_tmp = data_asian
group = 31
states = unique(data_tmp$state)

for (state in states){
  
  index = which(data_tmp$state == state)
  data_tmp_sub = data_tmp[index,]
  year=min(data_tmp_sub$year):2030
  st = rep(state, length(year))
  id = rep(group, length(year))
  
  yr = as.Date(paste(data_tmp_sub$year, 1, 1, sep = "-"))
  
  myts = xts(data_tmp_sub$under18/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  under18 = c(as.numeric(pred$x), as.numeric(pred$mean))
    
  myts = xts(data_tmp_sub$age18to34/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age18to34 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age35to64/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age35to64 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age65plus/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age65plus = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$totalPopulation/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  totalPopulation = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  df_state <- data.frame(under18=under18,
                         age18to34=age18to34, 
                         age35to64=age35to64,
                         age65plus=age65plus,
                         state=st,
                         raceID=id,
                         totalPopulation=totalPopulation,
                         year=year,
                         stringsAsFactors=FALSE)
  df = merge(df, df_state, all.x = TRUE, all.y =  TRUE)
}  
  

# black
data_tmp = data_black
group = 5
states = unique(data_tmp$state)

for (state in states){
  
  index = which(data_tmp$state == state)
  data_tmp_sub = data_tmp[index,]
  year=min(data_tmp_sub$year):2030
  st = rep(state, length(year))
  id = rep(group, length(year))
  
  yr = as.Date(paste(data_tmp_sub$year, 1, 1, sep = "-"))
  
  myts = xts(data_tmp_sub$under18/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  under18 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age18to34/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age18to34 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age35to64/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age35to64 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age65plus/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age65plus = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$totalPopulation/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  totalPopulation = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  df_state <- data.frame(under18=under18,
                               age18to34=age18to34, 
                               age35to64=age35to64,
                               age65plus=age65plus,
                               state=st,
                               raceID=id,
                               totalPopulation=totalPopulation,
                               year=year,
                               stringsAsFactors=FALSE)
  df = merge(df, df_state, all.x = TRUE, all.y =  TRUE)
}

# hispanic
data_tmp = data_hispanic
group = 400
states = unique(data_tmp$state)

for (state in states){
  
  index = which(data_tmp$state == state)
  data_tmp_sub = data_tmp[index,]
  year=min(data_tmp_sub$year):2030
  st = rep(state, length(year))
  id = rep(group, length(year))
  
  yr = as.Date(paste(data_tmp_sub$year, 1, 1, sep = "-"))
  
  myts = xts(data_tmp_sub$under18/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  under18 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age18to34/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age18to34 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age35to64/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age35to64 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age65plus/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age65plus = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$totalPopulation/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  totalPopulation = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  df_state <- data.frame(under18=under18,
                         age18to34=age18to34, 
                         age35to64=age35to64,
                         age65plus=age65plus,
                         state=st,
                         raceID=id,
                         totalPopulation=totalPopulation,
                         year=year,
                         stringsAsFactors=FALSE)
  df = merge(df, df_state, all.x = TRUE, all.y =  TRUE)
}

# white
data_tmp = data_white
group = 3
states = unique(data_tmp$state)

for (state in states){
  
  index = which(data_tmp$state == state)
  data_tmp_sub = data_tmp[index,]
  year=min(data_tmp_sub$year):2030
  st = rep(state, length(year))
  id = rep(group, length(year))
  
  yr = as.Date(paste(data_tmp_sub$year, 1, 1, sep = "-"))
  
  myts = xts(data_tmp_sub$under18/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  under18 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age18to34/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age18to34 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age35to64/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age35to64 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age65plus/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age65plus = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$totalPopulation/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  totalPopulation = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  df_state <- data.frame(under18=under18,
                         age18to34=age18to34, 
                         age35to64=age35to64,
                         age65plus=age65plus,
                         state=st,
                         raceID=id,
                         totalPopulation=totalPopulation,
                         year=year,
                         stringsAsFactors=FALSE)
  df = merge(df, df_state, all.x = TRUE, all.y =  TRUE)
}

# total
data_tmp = data_total
group = 1
states = unique(data_tmp$state)

for (state in states){
  
  index = which(data_tmp$state == state)
  data_tmp_sub = data_tmp[index,]
  year=min(data_tmp_sub$year):2030
  st = rep(state, length(year))
  id = rep(group, length(year))
  
  yr = as.Date(paste(data_tmp_sub$year, 1, 1, sep = "-"))
  
  myts = xts(data_tmp_sub$under18/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  under18 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age18to34/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age18to34 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age35to64/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age35to64 = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$age65plus/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  age65plus = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  myts = xts(data_tmp_sub$totalPopulation/1000, order.by = yr)
  fit = auto.arima(myts)
  pred = forecast(fit, 2030-max(strtoi(max(data_tmp_sub$year))))
  totalPopulation = c(as.numeric(pred$x), as.numeric(pred$mean))
  
  df_state <- data.frame(under18=under18,
                         age18to34=age18to34, 
                         age35to64=age35to64,
                         age65plus=age65plus,
                         state=st,
                         raceID=id,
                         totalPopulation=totalPopulation,
                         year=year,
                         stringsAsFactors=FALSE)
  df = merge(df, df_state, all.x = TRUE, all.y =  TRUE)
}


