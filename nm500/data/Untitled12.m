clear;

train3=load('train3.txt');

idx=kmeans(train3,4);

b=zeros([4 1000]);

current_i=ones([4 1]);

i=0;
h=0;
current=0;
temp=0;
count=2416;
mi=0;

result=zeros([2416 160]);

for i=1:2416
    current=idx(i);
    b(current,current_i(current))=i;
    current_i(current)=current_i(current)+1;
end

for h=1:4
    current_i(h)=current_i(h)-1;
end

mi=min(current_i);
mi=mi*4;
count=mi;

while count~=0
    for h=1:4
        temp=b(h,current_i(h));
        result(mi-count+1,:)=train3(temp,:);
        current_i(h)=current_i(h)-1;
        count=count-1;
    end
    
end

fid=fopen('train883.txt','wt');

for i= 1:mi
	fprintf(fid,'%3d,',result(i,:));
	fprintf(fid,'\n');
end

fclose(fid);

