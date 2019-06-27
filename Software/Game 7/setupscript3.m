%  -----To execute in Command Window---------
[ret, intletEEG] = MatNICEEGConnectLSL('NIC')
[ret, eeg_set, timestamp_set] = MatNICEEGRecordLSL(30, 20,intletEEG)
csvwrite('output-gameplay.csv',eeg_set)

%  --------Plot---------
%time = []
%time = timestamp_set(:)-timestamp_set(1)
%plot(time,detrend(eeg_set(:,1)))
%xlabel('Time(s)')
%ylabel('Voltage(uV)')
%plot(time,detrend(eeg_set(:,1)))

%  -------Extra-------
%[ret, accel_set, timestamp_set] = MatNICAccelRecordLSL(15, 'alberto')
%ret = MatNICStopEEG (socket) %Stop transimmion
%[ret, status] = MatNICQueryStatus (socket)    %Check transmission status

%  --------Markers-----
%[ret, outlet] = MatNICMarkerConnectLSL('Presentation')
%[ret] = MatNICMarkerSendLSL(2,outlet) 
%[ret] = MatNICMarkerSendLSL(1,outlet)
%[ret] = MatNICMarkerCloseLSL(outlet)  (End Marker Communication)
