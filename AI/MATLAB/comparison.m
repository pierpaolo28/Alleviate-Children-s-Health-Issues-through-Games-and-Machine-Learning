% filenames = {'TYP1.mat','ASD1.mat'};  
% for kk = 1:numel(filenames)
%     load(filenames{kk})
% end

% Plotting the EEG brainwaves of the first typical child on the left side 
% and of the first autistic child on the right side, this is done for all 
% the 5 feeatures (happy, neutral, etc..) and for their corrispondet
% experiment repetitions 1 and 35

% Plotting considering just one channel, all the timesteps and just one
% repetition

load TYP1.mat

data = struct2table(Stimulus);

rep1Thappy = data.Happy_data(1,:,1)
rep1Tneutral = data.Neutral_data(1,:,1)
rep1Tfear = data.Fear_data(1,:,1)
rep1Ttree = data.Tree_data(1,:,1)
rep1Tcartoon = data.Cartoon_data(1,:,1)

rep35Thappy = data.Happy_data(1,:,35)
rep35Tneutral = data.Neutral_data(1,:,35)
rep35Tfear = data.Fear_data(1,:,35)
rep35Ttree = data.Tree_data(1,:,35)
rep35Tcartoon = data.Cartoon_data(1,:,35)

load ASD1.mat

data2 = struct2table(Stimulus);

rep1Ahappy = data2.Happy_data(1,:,1)
rep1Aneutral = data2.Neutral_data(1,:,1)
rep1Afear = data2.Fear_data(1,:,1)
rep1Atree = data2.Tree_data(1,:,1)
rep1Acartoon = data2.Cartoon_data(1,:,1)


rep35Ahappy = data2.Happy_data(1,:,35)
rep35Aneutral = data2.Neutral_data(1,:,35)
rep35Afear = data2.Fear_data(1,:,35)
rep35Atree = data2.Tree_data(1,:,35)
rep35Acartoon = data2.Cartoon_data(1,:,35)

% Plotting considering all channels, all the timesteps and just one
% repetition

% load TYP1.mat
% 
% data = struct2table(Stimulus);
% 
% rep1Thappy = data.Happy_data(:,:,1);
% rep1Tneutral = data.Neutral_data(:,:,1);
% rep1Tfear = data.Fear_data(:,:,1);
% rep1Ttree = data.Tree_data(:,:,1);
% rep1Tcartoon = data.Cartoon_data(:,:,1);
% 
% rep35Thappy = data.Happy_data(:,:,35);
% rep35Tneutral = data.Neutral_data(:,:,35);
% rep35Tfear = data.Fear_data(:,:,35);
% rep35Ttree = data.Tree_data(:,:,35);
% rep35Tcartoon = data.Cartoon_data(:,:,35);
% 
% load ASD1.mat
% 
% data2 = struct2table(Stimulus);
% 
% rep1Ahappy = data2.Happy_data(:,:,1);
% rep1Aneutral = data2.Neutral_data(:,:,1);
% rep1Afear = data2.Fear_data(:,:,1);
% rep1Atree = data2.Tree_data(:,:,1);
% rep1Acartoon = data2.Cartoon_data(:,:,1);
% 
% 
% rep35Ahappy = data2.Happy_data(:,:,35);
% rep35Aneutral = data2.Neutral_data(:,:,35);
% rep35Afear = data2.Fear_data(:,:,35);
% rep35Atree = data2.Tree_data(:,:,35);
% rep35Acartoon = data2.Cartoon_data(:,:,35);
% 
figure1=figure('Position', [300, 300, 1224, 600]);

subplot(2,2,1)
plot(rep1Thappy)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,2)
plot(rep1Ahappy)
title('Atypical rythim')
%xlim([0,250])
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

subplot(2,2,3)
plot(rep35Thappy)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,4)
plot(rep35Ahappy)
title('Atypical rythim')
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

sgtitle('Typical vs Atypical EEG (Child 1 for both) - HappyData Rep1/35')

figure2=figure('Position', [300, 300, 1224, 600]);
subplot(2,2,1)
plot(rep1Tneutral)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,2)
plot(rep1Aneutral)
title('Atypical rythim')
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

subplot(2,2,3)
plot(rep35Tneutral)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,4)
plot(rep35Aneutral)
title('Atypical rythim')
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

sgtitle('Typical vs Atypical EEG (Child 1 for both) - NeutralData Rep1/35')

figure3=figure('Position', [300, 300, 1224, 600]);
subplot(2,2,1)
plot(rep1Tfear)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,2)
plot(rep1Afear)
title('Atypical rythim')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,3)
plot(rep35Tfear)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,4)
plot(rep35Afear)
title('Atypical rythim')
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

sgtitle('Typical vs Atypical EEG (Child 1 for both) - FearData Rep1/35')

figure4=figure('Position', [300, 300, 1224, 600]);
subplot(2,2,1)
plot(rep1Ttree)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,2)
plot(rep1Atree)
title('Atypical rythim')
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

subplot(2,2,3)
plot(rep35Ttree)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,4)
plot(rep35Atree)
title('Atypical rythim')
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

sgtitle('Typical vs Atypical EEG (Child 1 for both) - TreeData Rep1/35')

figure5=figure('Position', [300, 300, 1224, 600]);
subplot(2,2,1)
plot(rep1Tcartoon)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,2)
plot(rep1Acartoon)
title('Atypical rythim')
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

subplot(2,2,3)
plot(rep35Tcartoon)
title('Typical Rhythm')
ylabel('Amplitude (mV)')
xlabel('Channel Number')
xlim([0,128])

subplot(2,2,4)
plot(rep35Acartoon)
title('Atypical rythim')
xlabel('Channel Number')
ylabel('Amplitude (mV)')
xlim([0,128])

sgtitle('Typical vs Atypical EEG (Child 1 for both) - CartoonData Rep1/35')
