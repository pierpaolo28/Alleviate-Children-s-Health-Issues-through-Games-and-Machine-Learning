load ASD1.mat

% Convert a structure data type to table
data = struct2table(Stimulus);

% Mean, Variance and Standard Deviation going through all the repetitions


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

a = data.Happy_data(:,:,:);
V = a(:);

happymean21 = mean(V);
happyvar21 = var(V);
happystd21 = std(V);

a2 = data.Neutral_data(:,:,:);
V2 = a2(:);

neutralmean21 = mean(V2);
neutralvar21 = var(V2);
neutralstd21 = std(V2);

a3 = data.Tree_data(:,:,:);
V3 = a3(:);

treemean21 = mean(V3);
treevar21 = var(V3);
treestd21 = std(V3);

a4 = data.Fear_data(:,:,:);
V4 = a4(:);

fearmean21 = mean(V4);
fearvar21 = var(V4);
fearstd21 = std(V4);

a5 = data.Cartoon_data(:,:,:);
V5 = a5(:);

cartoonmean21 = mean(V5);
cartoonvar21 = var(V5);
cartoonstd21 = std(V5);
Vtot = cat(1, V, V2, V3, V4, V5);

child1mean21 = mean(Vtot);
child1var21 = var(Vtot);
child1std21 = std(Vtot);

save('children21.mat','happymean21','happystd21', 'neutralmean21','neutralvar21', 'neutralstd21','treemean21',...
    'treevar21','treestd21','fearmean21','fearvar21','fearstd21','cartoonmean21','cartoonvar21', 'cartoonstd21',...
    'child1mean21','child1var21','child1std21')