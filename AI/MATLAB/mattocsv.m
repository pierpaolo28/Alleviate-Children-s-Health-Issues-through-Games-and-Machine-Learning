 FileData = load('ASD12.mat');
 T = struct2table(FileData.Stimulus)
 writetable(T,'ASD12.csv','Delimiter',',')