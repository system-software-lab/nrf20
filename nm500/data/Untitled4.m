%result
c=[];
d=[];
%idx- check;
a=zeros([383 1]);
e=zeros([383 1]);
f=1;

i=0;


idx=kmeans(train3,383);

for i=1:2416
        if a(idx(i))==0
            %c=[c;train3(i,:)];
            c(idx(i),:)=train3(i,:);
            a(idx(i))=1;
            e(f)=idx(i);
            f=f+1;
        end
end



b=zeros([192 1]);

idx2=kmeans(train4,192);


for i=1:1218
    if b(idx2(i))==0
        %d=[d;train4(i,:)];
        d(idx2(i),:)=train4(i,:);
        b(idx2(i))=1;
    end
end

fid=fopen('train10.txt','wt');

for i=1:383
fprintf(fid,'%3d,',c(i,:));
fprintf(fid,'\n');
end

fclose(fid);

fid=fopen('train11.txt','wt');

for i=1:192
fprintf(fid,'%3d,',d(i,:));
fprintf(fid,'\n');
end

fclose(fid);

    