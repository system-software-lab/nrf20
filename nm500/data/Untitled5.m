clear;

train3=load('train3.txt');

idx=kmeans(train3,34);

a=zeros([34 200 160]);

b=ones([34 1]);

i=0;
h=0;
current=0;

result=[];

for i=1:2416
    current=idx(i);
    a(current,b(current),:)=train3(i,:);
    b(current)=b(current)+1;
end

%{
current=idx(1);
c=a(current,1,:);
%}

%{
current=0;
for i=1:2416
    if idx(i)==1
        current=current+1;
    end
end
%}

for i=1:2416:34
    for h=1:34
        if b(h)~=1
            result=[result;a(h,b(h-1),:)];
        end
    end
end
