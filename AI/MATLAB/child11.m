load TYP1.mat

data = struct2cell(Stimulus);
% child1 = load('data.mat')
% csvwrite('data.csv', child1);



% Option number 1, using structures

% Displaying stimolus array size
size(Stimulus.Happy_data)
size(Stimulus.Neutral_data)
size(Stimulus.Fear_data)
size(Stimulus.Tree_data)
size(Stimulus.Cartoon_data)

% [X,Y,Z] = xyz2grid(Stimulus.Happy_data(:,1),Stimulus.Happy_data(:,2),Stimulus.Happy_data(:,3)); 
% surf(X,Y,Z) 
% shading flat
% camlight

% Plotting a 3D plot for each stimulus repeated 80 times (just child 1)
% plot3(Stimulus.Happy_data(:,1),Stimulus.Happy_data(:,2),Stimulus.Happy_data(:,3));
% title('Stimulus Happy Data')
% figure
% scatter3(Stimulus.Happy_data(:,1),Stimulus.Happy_data(:,2),Stimulus.Happy_data(:,3))
% title('Stimulus Happy Data')

% plot3(Stimulus.Neutral_data(:,1),Stimulus.Neutral_data(:,2),Stimulus.Neutral_data(:,3));
% title('Stimulus Neutral Data')
% figure
% scatter3(Stimulus.Neutral_data(:,1),Stimulus.Neutral_data(:,2),Stimulus.Neutral_data(:,3))
% title('Stimulus Neutral Data')

% plot3(Stimulus.Fear_data(:,1),Stimulus.Fear_data(:,2),Stimulus.Fear_data(:,3));
% title('Stimulus Fear Data')
% figure
% scatter3(Stimulus.Fear_data(:,1),Stimulus.Fear_data(:,2),Stimulus.Fear_data(:,3))
% title('Stimulus Fear Data')

% plot3(Stimulus.Tree_data(:,1),Stimulus.Tree_data(:,2),Stimulus.Tree_data(:,3));
% title('Stimulus Tree Data')
% figure
% scatter3(Stimulus.Tree_data(:,1),Stimulus.Tree_data(:,2),Stimulus.Tree_data(:,3))
% title('Stimulus Tree Data')

% plot3(Stimulus.Cartoon_data(:,1),Stimulus.Cartoon_data(:,2),Stimulus.Cartoon_data(:,3));
% title('Stimulus Cartoon Data')
% figure
% scatter3(Stimulus.Cartoon_data(:,1),Stimulus.Cartoon_data(:,2),Stimulus.Cartoon_data(:,3))
% title('Stimulus Cartoon Data')

% Calculating the mean for each stimolus
% happymean = mean(Stimulus.Happy_data)
% neutralmean = mean(Stimulus.Neutral_data)
% fearmean = mean(Stimulus.Fear_data)
% treemean = mean(Stimulus.Tree_data)
% cartoonmean = mean(Stimulus.Cartoon_data)

% Calculating the variance for each stimolus
% happyvar = var(Stimulus.Happy_data)
% neutralvar = var(Stimulus.Neutral_data)
% fearvar = var(Stimulus.Fear_data)
% treevar = var(Stimulus.Tree_data)
% cartoonvar = var(Stimulus.Cartoon_data)

% Calculating the standard deviation for each stimolus
% happystd = std(Stimulus.Happy_data)
% neutralstd = std(Stimulus.Neutral_data)
% fearstd = std(Stimulus.Fear_data)
% treestd = std(Stimulus.Tree_data)
% cartoonstd = std(Stimulus.Cartoon_data)

% load TYP2.mat
% 
% size(Stimulus.Happy_data)
% size(Stimulus.Neutral_data)
% size(Stimulus.Fear_data)
% size(Stimulus.Tree_data)
% size(Stimulus.Cartoon_data)

% Option number 2 using a table

% Convert a structure data type to table
data = struct2table(Stimulus);

% % % Take a single column from the Happy Data (the last column)
% c = data.Happy_data(:,end);
% 
% % Take a single column from the Happy Data (column number 1) repetition n 1
% c2 = data.Happy_data(:,1,1);
% 
% % Take a sincle row from the Happy Data (row number 1) repetition number 1
% r = data.Happy_data(1,:,1);
% 
% % Take a sincle row from the Happy Data (row number 1) repetition number 80
% r2 = data.Happy_data(1,:,80);

figure
hold on
for i = 1:128
    dd = data.Happy_data(i, :, 1);
    size(dd)
    plot3(i.*ones(250),1:250, dd)
    title('EEG voltage across all the cahnnels, all time-steps (Repetition 1)')
    xlabel('Channel Number')
    ylabel('Time-step number')
    zlabel('Voltage (mV)')
end
hold off
% figure
% plot(1:250,r)
% %title('How the EEG voltage CH1 changes throughout one session repetition')
% hold on;
% scatter(1:128,data.Happy_data(:,2,1))
% %title('How the EEG voltage CH2 changes throughout one session repetition')
% hold on;
% scatter(1:128,data.Happy_data(:,3,1))
% title('How the EEG voltage CH1/CH2/CH3 changes throughout one session repetition')

% Test vmeans loop works
% vmean1 = mean(data.Happy_data(:,1,1))
% vmean2 = mean(data.Happy_data(:,2,1))
% vmean3 = mean(data.Happy_data(:,3,1))

% Creating an array filled of 128 zeroes and then filling it with the mean
% values of all the channels from 1 to 128 Happy Data (considering just
% repetition number 1)
% vmeansh11 = zeros(128,1)
% for i = 1:128
%     vmeansh11(i) = vmeansh11(i) + mean(data.Happy_data(:,i,1));
% end
% 
% totchannelsmeanh11 = mean(vmeansh11)
% 
% vmeansn11 = zeros(128,1)
% for i = 1:128
%     vmeansn11(i) = vmeansn11(i) + mean(data.Neutral_data(:,i,1));
% end
% 
% totchannelsmeann11 = mean(vmeansn11)
% 
% vmeansf11 = zeros(128,1)
% for i = 1:128
%     vmeansf11(i) = vmeansf11(i) + mean(data.Fear_data(:,i,1));
% end
% 
% totchannelsmeanf11 = mean(vmeansf11)
% 
% vmeanst11 = zeros(128,1)
% for i = 1:128
%     vmeanst11(i) = vmeanst11(i) + mean(data.Tree_data(:,i,1));
% end
% 
% totchannelsmeant11 = mean(vmeanst11)
% 
% vmeansc11 = zeros(128,1)
% for i = 1:128
%     vmeansc11(i) = vmeansc11(i) + mean(data.Cartoon_data(:,i,1));
% end
% 
% totchannelsmeanc11 = mean(vmeansc11)

% Mean, Variance and Standard Deviation going through all the repetitions

% new_data = zeros(128, 250);
% for i = 1:80
%     new_data = new_data + data.Happy_data(:, :, i);
% end
% 
% new_data = new_data./80;
% 
% figure
% hist(new_data(1, :), 15)
% figure
% hist(data.Happy_data(1, :, 1), 15)

% vstdh1 = zeros(128,1);
% vvarh1 = zeros(128,1);
% vmeansh1 = zeros(128,1);
% for j = 1:80
%     for i = 1:128
%         vmeansh1(i) = vmeansh1(i) + mean(data.Happy_data(i,:,j));
%         vvarh1(i) = vvarh1(i) + var(data.Happy_data(i,:,j));
%         vstdh1(i) = vstdh1(i) + std(data.Happy_data(i,:,j));
%     end
% end
% totchannelsmeanh1 = mean(vmeansh1)
% totchannelsvarh1 = var(vvarh1)
% totchannelsstdh1 = std(vstdh1)
% 
% vstdn1 = zeros(128,1);
% vvarn1 = zeros(128,1);
% vmeansn1 = zeros(128,1);
% for j = 1:80
%     for i = 1:128
%         vmeansn1(i) = vmeansn1(i) + mean(data.Neutral_data(i,:,j));
%         vvarn1(i) = vvarn1(i) + var(data.Neutral_data(i,:,j));
%         vstdn1(i) = vstdn1(i) + std(data.Neutral_data(i,:,j));
%     end
% end
% totchannelsmeann1 = mean(vmeansn1)
% totchannelsvarn1 = var(vvarn1)
% totchannelsstdn1 = std(vstdn1)
% 
% vstdf1 = zeros(128,1);
% vvarf1 = zeros(128,1);
% vmeansf1 = zeros(128,1);
% for j = 1:79
%     for i = 1:128
%         vmeansf1(i) = vmeansf1(i) + mean(data.Fear_data(i,:,j));
%         vvarf1(i) = vvarf1(i) + var(data.Fear_data(i,:,j));
%         vstdf1(i) = vstdf1(i) + std(data.Fear_data(i,:,j));
%     end
% end
% totchannelsmeanf1 = mean(vmeansf1)
% totchannelsvarf1 = var(vvarf1)
% totchannelsstdf1 = std(vstdf1)
% 
% vstdt1 = zeros(128,1);
% vvart1 = zeros(128,1);
% vmeanst1 = zeros(128,1);
% for j = 1:80
%     for i = 1:128
%         vmeanst1(i) = vmeanst1(i) + mean(data.Tree_data(i,:,j));
%         vvart1(i) = vvart1(i) + var(data.Tree_data(i,:,j));
%         vstdt1(i) = vstdt1(i) + std(data.Tree_data(i,:,j));
%     end
% end
% totchannelsmeant1 = mean(vmeanst1)
% totchannelsvart1 = var(vvart1)
% totchannelsstdt1 = std(vstdt1)
% 
% vstdc1 = zeros(128,1);
% vvarc1 = zeros(128,1);
% vmeansc1 = zeros(128,1);
% for j = 1:80
%     for i = 1:128
%         vmeansc1(i) = vmeansc1(i) + mean(data.Cartoon_data(i,:,j));
%         vvarc1(i) = vvarc1(i) + var(data.Cartoon_data(i,:,j));
%         vstdc1(i) = vstdc1(i) + std(data.Cartoon_data(i,:,j));
%     end
% end
% totchannelsmeanc1 = mean(vmeansc1)
% totchannelsvarc1 = var(vvarc1)
% totchannelsstdc1 = std(vstdc1)
% 
% vstim5mean = [totchannelsmeanh1, totchannelsmeann1, totchannelsmeanf1, totchannelsmeant1, totchannelsmeanc1];
% vstim5var = [totchannelsvarh1, totchannelsvarn1, totchannelsvarf1, totchannelsvart1, totchannelsvarc1];
% vstim5std = [totchannelsstdh1, totchannelsstdn1, totchannelsstdf1, totchannelsstdt1, totchannelsstdc1];
% 
% child1mean = mean(vstim5mean)
% child1var = var(vstim5var)
% child1std = std(vstim5std)

% meanchild = mean(mean(mean(data.Happy_data)))
% varchild = var(var(var(data.Happy_data)))
% stdchild = std(std(std(data.Happy_data)))

% child = [data.Happy_data(1:128,1:250,1:40) data.Fear_data(1:128,1:250,1:40) data.Tree_data(1:128,1:250,1:40) data.Cartoon_data(1:128,1:250,1:40) data.Neutral_data(1:128,1:250,1:40)]
% mchild = mean(child)
% vchild = var(child)
% schild = std(child)

% a = data.Happy_data(:,:,:);
% V = a(:);
% 
% happymean11 = mean(V);
% happyvar11 = var(V);
% happystd11 = std(V);
% 
% a2 = data.Neutral_data(:,:,:);
% V2 = a2(:);
% 
% neutralmean11 = mean(V2);
% neutralvar11 = var(V2);
% neutralstd11 = std(V2);
% 
% a3 = data.Tree_data(:,:,:);
% V3 = a3(:);
% 
% treemean11 = mean(V3);
% treevar11 = var(V3);
% treestd11 = std(V3);
% 
% a4 = data.Fear_data(:,:,:);
% V4 = a4(:);
% 
% fearmean11 = mean(V4);
% fearvar11 = var(V4);
% fearstd11= std(V4);
% 
% a5 = data.Cartoon_data(:,:,:);
% V5 = a5(:);
% 
% cartoonmean11 = mean(V5);
% cartoonvar11 = var(V5);
% cartoonstd11 = std(V5);
% 
% Vtot = cat(1, V, V2, V3, V4, V5);
% 
% child1mean11 = mean(Vtot);
% child1var11 = var(Vtot);
% child1std11 = std(Vtot);
% 
% size(Vtot);

% h = num2cell(data.Happy_data)
% 
% L = cellfun(@length,h);
% h = histogram(L);
% xticks(0:3000:18000);
% xticklabels(0:3000:18000);
% title('Signal Lengths')
% xlabel('Length')
% ylabel('Count')

% save('data.mat','data')

% save('children11.mat','happymean11','happystd11', 'neutralmean11','neutralvar11', 'neutralstd11','treemean11',...
%     'treevar11','treestd11','fearmean11','fearvar11','fearstd11','cartoonmean11','cartoonvar11', 'cartoonstd11',...
%     'child1mean11','child1var11','child1std11')


%  FileData = load('ASD1.mat');
%  T = struct2table(FileData.Stimulus)
%  writetable(T,'myData.csv','Delimiter',',')